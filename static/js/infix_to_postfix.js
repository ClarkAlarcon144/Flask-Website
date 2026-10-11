const eventData = document.getElementById("event-data");

if (eventData) {
    const events = JSON.parse(eventData.textContent);

    // Shared playback state
    let index = 0;
    let history = [];
    let isPlaying = false;
    let timer = null;

    const playPauseButton = document.getElementById("play-pause");
    const currentToken = document.getElementById("value");
    const instruction = document.getElementById("instruction");

    function updateCurrentToken(event) {
        currentToken.textContent = `${event.value}`;

        let action = event.action;
        let stack = event.stack;
        let connector;
        
        if (action === 'push') {
            action = 'pushed';
            connector =  "to";
        }

        if (action === 'pop') {
            action = 'popped';
            connector = 'from';
        }

        instruction.textContent = `${action} ${connector} ${stack}`;
    }

    // Apply one event and return the instruction to undo it.
    function applyEvent(event) {
        const stack = document.getElementById(event.stack);

        if (!stack) {
            console.error("Stack not found:", event.stack);
            return null;
        }

        if (event.action === "push") {
            const node = document.createElement("div");
            node.className = "node";
            node.textContent = event.value;
            stack.prepend(node);

            // Undoing a push means popping.
            return {
                stack: event.stack,
                action: "pop"
            };
        }

        if (event.action === "pop") {
            const node = stack.firstElementChild;

            if (!node) return null;

            // Save the value BEFORE removing the node.
            const value = node.textContent;
            node.remove();

            // Undoing a pop means pushing the value back.
            return {
                stack: event.stack,
                action: "push",
                value: value
            };
        }

        return null;
    }



    // Execute one event.
    function stepForward() {
        if (index >= events.length) return;

        const event = events[index];

        updateCurrentToken(event);

        const undoEvent = applyEvent(event);

        history.push(undoEvent);
        index++;
    }

    // Reverse the most recently executed event.
    function stepBackward() {
        if (index <= 0) return;

        const undoEvent = history.pop();

        if (undoEvent) {
            applyEvent(undoEvent);
        }

        index--;

        if (index > 0) {
            updateCurrentToken(events[index - 1]);
        } else {
            currentToken.textContent = "";
            instruction.textContent = "";
        }
    }

    // Clear everything and return to the initial state.
    function resetVisualizer() {
        pause();

        document.getElementById("operators").innerHTML = "";
        document.getElementById("output").innerHTML = "";

        currentToken.textContent = "";
        instruction.textContent = "";

        history = [];
        index = 0;
    }

    // Play events automatically.
    function play() {
        if (isPlaying) return;

        isPlaying = true;
        playNextEvent();
        playPauseButton.textContent = "⏸";
    }

    function playNextEvent() {
        if (!isPlaying) return;

        if (index >= events.length) {
            pause();
            return;
        }

        stepForward();
        timer = setTimeout(playNextEvent, 700);
    }

    // Stop automatic playback.
    function pause() {
        isPlaying = false;
        clearTimeout(timer);
        timer = null;
        playPauseButton.textContent = "▶";
    }

    // Jump to the end without delays.
    function fastForward() {
        pause();

        while (index < events.length) {
            stepForward();
        }
    }

    // Connect the functions to the HTML buttons.
    document.getElementById("rewind").addEventListener("click", resetVisualizer);

    document.getElementById("step-back").addEventListener("click", () => {
        pause();
        stepBackward();
    });

    document.getElementById("play-pause").addEventListener("click", () => {
        if (isPlaying) {
            pause();
        } else if (index >= events.length) {
            return;
        } else {
            play();
        }
    });

    document.getElementById("step-forward").addEventListener("click", () => {
        pause();
        stepForward();
    });

    document.getElementById("fast-forward").addEventListener("click", fastForward);

    play()
}

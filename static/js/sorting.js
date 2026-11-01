
const bars = document.getElementById("bars");
const statusText = document.getElementById("status");
const algorithmName = document.getElementById("algorithm-name");

const delay = (ms) =>
    new Promise(resolve => setTimeout(resolve, ms));

function drawBars(arr, active = [], sorted = []) {

    bars.innerHTML = "";

    const maxValue = Math.max(...arr, 1);

    arr.forEach((value, index) => {

        const bar = document.createElement("div");
        bar.classList.add("bar");

        if (sorted.includes(index)) {
            bar.style.backgroundColor = "#22c55e";
        }
        else if (active.includes(index)) {
            bar.style.backgroundColor = "#f59e0b";
        }
        else {
            bar.style.backgroundColor = "#3b82f6";
        }

        bar.style.height =
            Math.max(25, (value / maxValue) * 250) + "px";

        const label = document.createElement("span");
        label.textContent = value;

        bar.appendChild(label);
        bars.appendChild(bar);

    });
}


// BUBBLE SORT
async function bubbleSort(arr) {

    let n = arr.length;

    for (let i = 0; i < n; i++) {

        for (let j = 0; j < n - i - 1; j++) {

            drawBars(arr, [j, j + 1]);
            await delay(300);

            if (arr[j] > arr[j + 1]) {

                [arr[j], arr[j + 1]] =
                [arr[j + 1], arr[j]];

                drawBars(arr, [j, j + 1]);
                await delay(300);
            }
        }
    }

    return arr;
}


// SELECTION SORT
async function selectionSort(arr) {

    let n = arr.length;

    for (let i = 0; i < n; i++) {

        let minIndex = i;

        for (let j = i + 1; j < n; j++) {

            drawBars(arr, [minIndex, j]);
            await delay(300);

            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }

        [arr[i], arr[minIndex]] =
        [arr[minIndex], arr[i]];

        drawBars(arr, [i, minIndex]);
        await delay(300);
    }

    return arr;
}


// INSERTION SORT
async function insertionSort(arr) {

    for (let i = 1; i < arr.length; i++) {

        let key = arr[i];
        let j = i - 1;

        while (j >= 0 && arr[j] > key) {

            drawBars(arr, [j, j + 1]);
            await delay(300);

            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = key;

        drawBars(arr, [j + 1]);
        await delay(300);
    }

    return arr;
}


// MERGE SORT
async function mergeSort(arr, start = 0) {

    if (arr.length <= 1) {
        return arr;
    }

    let mid = Math.floor(arr.length / 2);

    let left = await mergeSort(arr.slice(0, mid), start);
    let right = await mergeSort(
        arr.slice(mid),
        start + mid
    );

    let merged = [];

    let i = 0;
    let j = 0;

    while (i < left.length && j < right.length) {

        if (left[i] <= right[j]) {
            merged.push(left[i]);
            i++;
        }
        else {
            merged.push(right[j]);
            j++;
        }
    }

    merged.push(...left.slice(i));
    merged.push(...right.slice(j));

    for (let k = 0; k < merged.length; k++) {
        arr[k] = merged[k];
    }

    drawBars(arr, arr.map((_, i) => i));
    await delay(400);

    return arr;
}


// QUICK SORT
async function quickSort(arr, low = 0, high = arr.length - 1) {

    if (low < high) {

        let pivot = arr[high];
        let i = low - 1;

        for (let j = low; j < high; j++) {

            drawBars(arr, [j, high]);
            await delay(300);

            if (arr[j] < pivot) {

                i++;

                [arr[i], arr[j]] =
                [arr[j], arr[i]];

                drawBars(arr, [i, j]);
                await delay(300);
            }
        }

        [arr[i + 1], arr[high]] =
        [arr[high], arr[i + 1]];

        let pivotIndex = i + 1;

        drawBars(arr, [pivotIndex]);
        await delay(300);

        await quickSort(arr, low, pivotIndex - 1);
        await quickSort(arr, pivotIndex + 1, high);
    }

    return arr;
}


// RUN SELECTED ALGORITHM
async function startSorting() {

    if (!numbers || numbers.length === 0) {
        return;
    }

    let arr = [...numbers];

    algorithmName.textContent =
        algorithm.toUpperCase() + " SORT";

    statusText.textContent = "Sorting in progress...";

    drawBars(arr);

    await delay(500);

    if (algorithm === "bubble") {
        await bubbleSort(arr);
    }

    else if (algorithm === "selection") {
        await selectionSort(arr);
    }

    else if (algorithm === "insertion") {
        await insertionSort(arr);
    }

    else if (algorithm === "merge") {
        await mergeSort(arr);
    }

    else if (algorithm === "quick") {
        await quickSort(arr);
    }

    drawBars(arr, [], arr.map((_, i) => i));

    statusText.textContent = "Sorting completed!";
}

startSorting();

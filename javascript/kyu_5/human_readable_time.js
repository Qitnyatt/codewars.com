// https://www.codewars.com/kata/52685f7382004e774f0001f7/train/javascript

const humanReadable = (seconds) => {
    const result = [];
    [3600, 60, 1].forEach((interval, index, array) => {
        result.push(Math.floor(seconds / interval));
        if (Math.floor(seconds / interval)) {
            seconds = seconds % interval;
        }
    });
    return result.map(x => x.toString().padStart(2, '0')).join(':');
}

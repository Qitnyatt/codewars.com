const fakeBin = (x) => x
    .split('')
    .map(currentValue => parseInt(currentValue, 10) < 5 ? '0' : '1')
    .join('');

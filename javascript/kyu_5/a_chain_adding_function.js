// https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/train/javascript


const add = (n) => {
    const f = (x) => add(n + x);
    f.valueOf = () => n;
    return f;
}

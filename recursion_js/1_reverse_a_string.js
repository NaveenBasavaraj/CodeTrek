function reverseString(s) {
    if (s.length === 0 || s.length === 1) {
        return s; // base case: string of length 0 or 1 is already reversed
    }
    // what is the smallest amount of work I can do in each iteration?
    return reverseString(s.slice(1)) + s[0];
}

s = reverseString("Hello World")
console.log(s)

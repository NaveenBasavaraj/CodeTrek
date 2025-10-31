function decimalToBinary(decimal, result = "") {
    if (decimal === 0) {
        return result || "0"; // handle input 0
    }
    result = (decimal % 2) + result;
    return decimalToBinary(Math.floor(decimal / 2), result);
}

console.log(decimalToBinary(0));  // "0"
console.log(decimalToBinary(1));  // "1"
console.log(decimalToBinary(2));  // "10"
console.log(decimalToBinary(5));  // "101"
console.log(decimalToBinary(10)); // "1010"
console.log(decimalToBinary(19)); // "10011"
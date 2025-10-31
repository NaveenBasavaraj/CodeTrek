function is_palindrome(s) {
    // base case or stopping condition
    if (s.length === 0 || s.length === 1) {
        return true
    }
    // do some work to shrink the problem space
    if (s[0] === s[s.length - 1]) {
        return is_palindrome(s.slice(1, -1))
    }
    return false
}

console.log(is_palindrome("KAYAK"))
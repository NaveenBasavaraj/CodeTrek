class Stack {
    constructor() {
        this.stack = [];
    }

    is_empty() {
        if (this.stack.length == 0) {
            return true;
        }
        return false;
    }

    push(item) {
        this.stack.push(item);
    }

    pop() {
        if (this.is_empty()){
            return "Stack IS Empty";
        }
        return this.stack.pop();
    }

    peek(){
        if (this.is_empty()){
            return "Stack IS Empty";
        }
        return this.stack[this.stack.length - 1];
    }

    size(){
        return this.stack.length;
    }


};



const s = new Stack();
s.push(10);
s.push(20);
console.log(s.peek());  // 20
console.log(s.pop());   // 20
console.log(s.is_empty());  // false
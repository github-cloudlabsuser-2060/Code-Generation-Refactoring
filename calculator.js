/**Create a simple calculator that can perform addition, subtraction, multiplication, and division**/

/**
 * Unified calculator function.
 * If passed an array, performs batch calculations.
 * If passed operation, a, b, performs a single calculation.
 * @param {'add'|'subtract'|'multiply'|'divide'|Array<{operation: 'add'|'subtract'|'multiply'|'divide', a: number, b: number}>} operationOrBatch
 * @param {number} [a]
 * @param {number} [b]
 * @returns {number|number[]}
 */
function calculator(operationOrBatch, a, b) {
    if (Array.isArray(operationOrBatch)) {
        return operationOrBatch.map(op => calculator(op.operation, op.a, op.b));
    }
    switch (operationOrBatch) {
        case 'add':
            return add(a, b);
        case 'subtract':
            return subtract(a, b);
        case 'multiply':
            return multiply(a, b);
        case 'divide':
            return divide(a, b);
        default:
            throw new Error('Invalid operation');
    }
}

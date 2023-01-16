let l: number[];
/**
 * What is the different between these 4 loops and their results?
 * What is:
 *  - value of `a`
 *  - value of `b`
 *  - value of `l` after a is set
 *  - value of `l` after b is set
 *  - value of `l` after for..of loop
 *  - value of `l` after for..in loop
 */

l = [1, 2, 3, 4, 5];
const a = l.map(n => n * 2);
// console.log('a:', a);
// console.log('l after a:', l);

l = [1, 2, 3, 4, 5];
const b = l.forEach(n => (n *= 2));
// console.log('b:', b);
// console.log('l after b:', l);

l = [1, 2, 3, 4, 5];
for (let i in l) l[i] *= 2;
// console.log('l after for..in:', l);

l = [1, 2, 3, 4, 5];
for (let n of l) n *= 2;
// console.log('l after for..of:', l);

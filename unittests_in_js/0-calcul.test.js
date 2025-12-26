const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function () {
  describe('rounding of first number', function () {
    it('should return 4 when a=1 and b=3', function () {
      assert.strictEqual(calculateNumber(1, 3), 4);
    });

    it('should return 5 when a=1.2 and b=3.7', function () {
      assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });

    it('should return 6 when a=1.5 and b=3.7', function () {
      assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });
  });

  describe('rounding of second number', function () {
    it('should return 5 when a=1 and b=3.7', function () {
      assert.strictEqual(calculateNumber(1, 3.7), 5);
    });
  });
});

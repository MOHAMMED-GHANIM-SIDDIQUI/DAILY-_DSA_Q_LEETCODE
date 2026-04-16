#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";

        string result;

        // Handle sign
        if ((numerator < 0) ^ (denominator < 0)) result += "-";

        // Convert to long to avoid overflow
        long n = labs((long)numerator);
        long d = labs((long)denominator);

        // Integer part
        result += to_string(n / d);
        long remainder = n % d;

        if (remainder == 0) return result; // no fractional part

        result += ".";

        unordered_map<long, int> seen; // remainder -> position in result

        while (remainder != 0) {
            if (seen.count(remainder)) {
                // Insert "(" at the first occurrence
                result.insert(seen[remainder], "(");
                result += ")";
                break;
            }

            seen[remainder] = result.size();

            remainder *= 10;
            result += to_string(remainder / d);
            remainder %= d;
        }

        return result;
    }
};

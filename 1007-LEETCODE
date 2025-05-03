class Solution {
public:
    int minDominoRotations(vector<int>& A, vector<int>& B) {
        // Try to make all values in A and B equal to the values from A[0] or B[0]
        int min_rotations = min(helper(A, B, A[0]), helper(A, B, B[0]));
        
        // If neither A[0] nor B[0] could result in a valid solution, return -1
        return min_rotations == INT_MAX ? -1 : min_rotations;
    }
    
    int helper(vector<int>& A, vector<int>& B, int x) {
        int rotationsA = 0, rotationsB = 0;
        
        for (int i = 0; i < A.size(); ++i) {
            // If x doesn't appear in either A[i] or B[i], it's not possible
            if (A[i] != x && B[i] != x) return INT_MAX;
            
            // Count the number of rotations needed to make A[i] or B[i] equal to x
            if (A[i] != x) rotationsA++;
            else if (B[i] != x) rotationsB++;
        }
        
        return min(rotationsA, rotationsB);
    }
};

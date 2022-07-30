using namespace std;
#include <vector>
bool isValidSubsequence(vector<int> array, vector<int> sequence)
{
    // Write your code here.
    int jdx = 0;
    int countI = 0;
    for (int i = 0; i < sequence.size(); i++)
    {
        for (int j = jdx; j < array.size(); j++)
        {
            if (sequence[i] == array[j])
            {
                jdx = j + 1;
                countI += 1;
                break;
                if (j == array.size() - 1)
                    return false;
            }
        }
    }
    if (countI == sequence.size())
        return true;
    return false;
}
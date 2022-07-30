#include <vector>
using namespace std;

vector<int> sortedSquaredArray(vector<int> array)
{
    // Write your code here.
    int i = 0;
    int j = array.size() - 1;
    vector<int> result(array.size(), 0);
    for (int k = j; k >= 0; k--)
    {
        if (abs(array[i]) > abs(array[j]))
        {
            result[k] = array[i] * array[i];
            i += 1;
        }
        else
        {
            result[k] = array[j] * array[j];
            j -= 1;
        }
    }
    return result;
}
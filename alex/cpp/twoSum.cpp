#include <vector>
#include <unordered_map>

using namespace std;

vector<int> twoNumberSum(vector<int> array, int targetSum)
{
    // Write your code here.
    unordered_map<int, int> table;
    int n = array.size();
    int remain;
    for (int i = 0; i < n; i++)
    {
        remain = targetSum - array[i];
        if (table.find(array[i]) == table.end())
            table[remain] = i;
        else
            return {array[i], remain};
    }
    return {};
}

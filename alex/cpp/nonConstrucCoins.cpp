#include <vector>
using namespace std;

int nonConstructibleChange(vector<int> coins)
{
    // Write your code here.
    sort(coins.begin(), coins.end());
    int sumPre = 0;
    for (int i = 0; i < coins.size(); i++)
    {

        if (sumPre + 1 < coins[i])
            return sumPre + 1;
        sumPre += coins[i];
    }
    return sumPre + 1;
}

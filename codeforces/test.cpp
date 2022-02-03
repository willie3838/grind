#include <vector>
#include <set>
#include <iostream>
#include <cmath>
#include <string>
using namespace std;
 
 /*
 123

 321

 a = 31
 b = 2
 */
vector<string> permutations(vector<string> res, string N, int l, int r){
    if(l == r){
        cout << N << endl;
        res.push_back(N);
        return res;
    }

    for(int i = l; i < N.size(); i++){
        swap(N[l], N[i]);
        permutations(res, N, l+1, r);
        swap(N[l], N[i]);
    }
    return res;
}
 
int main(){

    string s = "hello";
    cout << s.substr(0, 0) << endl;

    // int ans = 0;
    // string N;
    // cin >> N;
    // sort(N.begin(), N.end());

    // do{
    //     for(int i = 1; i < N.size(); i++){
    //         int l = 0, r = 0;
    //         for(int j = 0; j < i; j++){
    //             l = l * 10 + N[j] - '0';
    //         }
    //         for(int j = i; j < N.size(); j++){
    //             r = r * 10 + N[j] - '0';
    //         }
    //         ans = max(ans, l*r);
    //     }
    // }while(next_permutation(N.begin(), N.end()));
    
    // cout << ans << endl;
    // cout << '9' - '0' << endl;
    // return 0;

}
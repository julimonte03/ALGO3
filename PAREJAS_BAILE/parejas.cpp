// Tenemos dos conjuntos de personas y para cada persona sabemos su habilidad de baile. Queremos
// armar la máxima cantidad de parejas de baile, sabiendo que para cada pareja debemos elegir
// exactamente una persona de cada conjunto de modo que la diferencia de habilidad sea menor o
// igual a 1 (en módulo). Además, cada persona puede pertenecer a lo sumo a una pareja de baile.
// Por ejemplo, si tenemos un multiconjunto con habilidades {1, 2, 4, 6} y otro con {1, 5, 5, 7, 9}, la
// máxima cantidad de parejas es 3. Si los multiconjuntos de habilidades son {1, 1, 1, 1, 1} y {1, 2, 3},
// la máxima cantidad es 2.
#include <iostream>
#include <vector>
using namespace std;

int maxDancePairs(vector<int>& l1, vector<int>& l2) {
    int i = 0, j = 0;
    int res = 0;

    while (i < l1.size() && j < l2.size()) {
        if (abs(l1[i] - l2[j]) <= 1) {
            res++; 
            i++; 
            j++; 
        } 
        
        else if (l1[i] < l2[j]) {
            i++;
        } else {
            j++;
        }
    }

    return res; 
}

int main() {
   vector<int> l1 = {1, 2, 4, 6};
   vector<int> l2 = {1, 5, 5, 7, 9};

    int result = maxDancePairs(l1, l2);
   cout << result <<endl;

    return 0;
}

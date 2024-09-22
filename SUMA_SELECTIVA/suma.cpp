// Dado un conjunto X con |X| = n y un entero k ≤ n queremos encontrar el máximo valor que
// pueden sumar los elementos de un subconjunto S de X de tamaño k.

#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;
//ordeno de forma ascendente, selecciono los k elementos mas grande y calculo la sumatoria
pair<int, vector<int>> sumaSelectiva(vector<int> &X, int k) {
    sort(X.begin(), X.end(), greater<int>());
    
    vector<int> S(X.begin(), X.begin() + k);
    
    int suma = accumulate(S.begin(), S.end(), 0);
    
    return {suma, S};
}

int main() {
    vector<int> X = {5, 1, 3, 9, 2};
    int k = 3;
    auto resultado = sumaSelectiva(X, k);
    
    cout << "Suma maxima: " << resultado.first << endl;
    cout << "Subconjunto: ";
    for (int elem : resultado.second) {
        cout << elem << " ";
    }
    cout << endl;
    
    return 0;
}

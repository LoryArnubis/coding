#include <iostream>

using namespace std;

int max(int x, int y)
{
	if(x > y){
		return x;
	}
	return y;
}

int main()
{
	int a,b,sum;
	cin >> a >> b;
	cout <<"max is " << max(a, b) << endl;
	return 0;
}

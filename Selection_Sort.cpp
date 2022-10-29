#include <iostream>
using namespace std;
int* rdm(int n)
{
   int b;
   int *arr=new int[n];
	srand(time(0));
	for(int i=0;i<n;i++)
	{
    	b=1+(rand()%100);
     	arr[i]=b;
	}
	return arr;
}
int main()
{
	int n,a;
	cout<<"input the size of the array = ";
	cin>>n;
	int* ptr;
	ptr=rdm(n);
	cout<<"our randam array = "<<" ";
	for(int i=0;i<n;i++)
	cout<<ptr[i]<<" ";
	for(int i=0;i<(n-1);i++)
	{
    		int min=i;
    	for(int j=(i+1);j<n;j++)
    	{
        		if(ptr[min]>ptr[j])
  	            min=j;
        	}
        	if(min!=i)
        	{
                 int temp=ptr[min];
                 ptr[min]=ptr[i];
                 ptr[i]=temp;
        	}
        	cout<<endl;
   	cout<<"array after "<<i+1<<" pass = ";
    	for(int k=0;k<n;k++)
    	{
        	cout<<ptr[k]<<" ";
    	}
    	cout<<endl;
	}
	cout<<"sorted array = "<<" ";
	for(int i=0;i<n;i++)
               cout<<ptr[i]<<" ";
	return 0;
}

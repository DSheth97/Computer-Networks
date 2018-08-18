//#include<iostream>
#include <stdio.h>
#include<conio.h>
#include <string.h>
#include<fstream.h>
//using namespace std;


long generate(int i)
{
    long n=i^(3/2);
    return n;
}

void A000093()
{
    cout<<"Hello";
ifstream fin;
ofstream fout;
char line[100];
long r,n;
int i=0;
fin.open("File.txt");
while(!fin.fail())
{
fin>>n;
while(!fin.eof())
{
      // fin>>n;
       cout<<"N= "<<n;
	fin.getline(line,100,'\n');

	if(i<50)
	{
	cout<<"Line= "<<line;
	r=generate(i);
	i++;
	cout<<"R= "<<r;
	}

       //	if()
	//{
	    cout<<r;
	    fout<<line<<"A000093"<<endl;
	//}
    }
}
}
void main()
{
    clrscr();
    A000093();
    //	return 0;
    getch();
}


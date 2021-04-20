#include<bits/stdc++.h>
using namespace std;
char a[3][3]={{'1','2','3'},{'4','5','6'},{'7','8','9'}};
int row,col;
char turn='x';
bool draw=false;
int display()
{
system("cls");
cout<<"___________________________________ welcome to the world of ZERO-CROSS GAME___________________________________________"<<endl;
 cout<<"player 1 : x\n player 2 : o"<<endl<<endl<<endl;
 cout<<"Let the game begin.........."<<endl<<endl;
 cout<<"\t\t     |     |     \n";
 cout<<"\t\t  "<<a[0][0]<<"  |  "<<a[0][1]<<"  |  "<<a[0][2]<<"  \n";
 cout<<"\t\t_____|_____|_____\n";
 cout<<"\t\t     |     |     \n";
 cout<<"\t\t  "<<a[1][0]<<"  |  "<<a[1][1]<<"  |  "<<a[1][2]<<"  \n";
 cout<<"\t\t_____|_____|_____\n";
 cout<<"\t\t     |     |     \n";
 cout<<"\t\t  "<<a[2][0]<<"  |  "<<a[2][1]<<"  |  "<<a[2][2]<<"  \n";
 cout<<"\t\t     |     |     \n";
}
int player_turn()
{
    int c;
    if(turn=='x')
    {
  cout<<"player 1  turn:  ";
    }
    if(turn=='o')
    {
  cout<<"player 2  turn:  ";
    }
 cin>>c;
 switch(c)
 {
case 1: row=0;col=0;break;
case 2: row=0;col=1;break;
case 3: row=0;col=2;break;
case 4: row=1;col=0;break;
case 5: row=1;col=1;break;
case 6: row=1;col=2;break;
case 7: row=2;col=0;break;
case 8: row=2;col=1;break;
case 9: row=2;col=2;break;
default:
cout<<"invalid"<<endl;
break;
    }
    if(turn=='x'&&a[row][col]!='x'&&a[row][col]!='o')
    {
        a[row][col]='x';
        turn='o';
    }
   else if(turn=='o'&&a[row][col]!='x'&&a[row][col]!='o')
    {
        a[row][col]='o';
        turn='x';
        }
        else{
            cout<<"value already assigned \nplease try again!!..\n\n"<<endl;
            player_turn();
        }
        display();
}
bool gameover()
{
    //check win
    int i,j;
    for(i=0;i<3;i++)
        if(a[i][0]==a[i][1]&&a[i][0]==a[i][2]||a[0][i]==a[1][i]&&a[0][i]==a[2][i])
    return false;
    if(a[0][0]==a[1][1]&&a[0][0]==a[2][2]||a[0][2]==a[1][1]&&a[0][2]==a[2][0])
        return false;
    for(i=0;i<3;i++)
    for(j=0;j<3;j++)
        if(a[i][j]!='x'&&a[i][j]!='o')
        return true;
        draw= true;
        return false;

}
 int main()
{
    while(gameover())
    {

        display();
        player_turn();
        display();

    }
    if(turn=='o'&& draw == false)

    cout<<"......................CONGRATULATIONS!!..................\n\n\n_____________PLAYER 1[X] WON!!!! "<<endl<<endl<<endl;

    else if(turn=='x'&& draw == false)
        cout<<"CONGRATULATIONS!!.....\n\n\nPLAYER 2[o] WON!! "<<endl;

    else
    cout<<"GAME DRAW!!"<<endl;


}

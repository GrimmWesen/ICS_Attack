# bool isInt(char s[]){
#    for (int i = 0; s[i] != '\0'; i++)
#    if (!isdigit(s[i])){
# 	return false;
#    }

#     return true;
# }

# int main() {
# 	int cnt = 0;
# 	int guess = VALUE+1;
#     char input [12];
#     cout<<"Welcome to Guess-Num!"<<endl;
# 	cout<<"I have preset an integer value,Please input one Integer to guess it,and I'll tell you big or small " <<endl;
# 	cout<<"Please input one integer:"<<endl;
# 	while(guess!=VALUE){
# 		while(cin>>input && !isInt(input)){
# 			cout << "Invalid ! Please input an integer!:";
# 			getchar();
# 		}
# 		guess = atoi(input);//转int
# 		if(guess>VALUE){
# 			cnt++;
# 			cout<<BIG<<endl;
# 		}
# 		else if(guess<VALUE){
# 			cnt++;
# 			cout<<SMALL<<endl;
# 		} 
# 		else{
# 			cout<<"Awesome！"<<endl;
# 			cout<<"total guess num:"<<cnt<<endl; 
# 		}
# 	} 
# }
# bool isInt(char s[]){
    # if(s[0]=='\0'){
    #   return false;
    # }
#   for (int i = 0; s[i] != '\0'; i++){
#   	 if(!isdigit(s[i])){
#   		 if(i==0&&s[i]=='+'||s[i]=='-'){
#   			return true;
# 		  }
# 		  return false;
# 	 } 
#   }
#     return true;
# }
# int atoi(string s){
#    $t3 = decbuf;
#    $a0 = 0;
#    $t2 = 0($t3);
#    if ( $t2 ='-'  )  $a2 =1;
#    $t3++;
#    $t2 = 0($t3);
#    while ( ($t2 != '\n' || $t2 != '\0') && ( '0' <= $t2 <= '9')) {
#           $t2 -= 0x30;
#           $a0 *= 10;
#           $a0 += $t2;
#           $t3++;
#           $t2 = 0($t3);
#    };
#    if ( $t2 <'0' || $t2 > '9') {
#               cout << err_msg;
#               exit;
#    };
#    if ($a2) neg $a0; 
#    cout << number;
#    return number;  
# }
# int main()
# {
# 	string dates;
# 	cout<<"input date:";
# 	cin>> dates;
# 	cout<<"input n:";
#     int days;  
# 	  cin>>days;
#     Date date;
    date.year = atoi(dates.substring(0,4));
    date.month = atoi(dates.substring(5,2));
    date.day = atoi(dates.substring(8,2));
#     cout<<date.year<<" "<<date.month<<" "<<date.day<<endl;
#     date = whichDate(date,days);
#     printf("%4d-%02d-%02d",date.year,date.month,date.day);
#     return 0; 
# }
# struct Date {
#     int year;
#     int month;
#     int day;
# };
# Date whichDate(Date date, int days){

#     days += (date.day -1);
#     date.day = 1;

#     //计算当前月份天数
#     int day = 0;
#     switch(date.month){
#     case 1:
#     case 3:
#     case 5:
#     case 7:
#     case 8:
#     case 10:
#     case 12:
#         day = 31;
#         break;
#     case 4:
#     case 6:
#     case 9:
#     case 11:
#         day = 30;
#         break;
#     case 2:
#         if((date.year % 4 == 0 && date.year % 100 !=0) || date.year % 400 == 0){//闰年的判断 
#             day = 29;
#         }
#         else {
#             day = 28;
#         }
#         break;
#     }
#     if (days - day >= 0)
#     {
#         if (date.month == 12)
#         {
#             date.year += 1;
#             date.month = 1;
#         }
#         else{
#             date.month += 1;
#         }
#         return whichDate(date,days-day);

#     }
#     else {
#         date.day += days;
#     }
#     return date;
# }
Date getDate(String s){
	Date date;
	date.year = atoi(dates.substring(0,4));
    date.month = atoi(dates.substring(5,2));
    date.day = atoi(dates.substring(8,2));

}






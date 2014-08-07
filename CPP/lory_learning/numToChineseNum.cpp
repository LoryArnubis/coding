//
//  main.cpp
//  numToChineseNum
//
//  Created by tyn on 14-7-28.
//  Copyright (c) 2014年 waimai. All rights reserved.
//

#include <iostream>
#include <vector>
#include <cmath>
#include <float.h>

#define LL long long
#define MIN 0.0000001

using namespace std;

const vector<string> chinese_num = {"零","壹","贰","叁","肆","伍","陆","柒","捌","玖"};
const vector<string> chinese_unit = {"拾","佰","仟"};
const vector<string> chinese_bigunit = {"圆","萬","亿"};
const vector<string> chinese_float = {"角","分"};

//判断数字符号
bool isPositive(double inputNum)
{
    return inputNum>=0?true:false;
}

//处理可能存在的小数部分，只取前两位小数，忽略其他
string processFloat(float inputNum)
{
    string result = "";
    LL roundNum = static_cast<LL>(inputNum*100);
    if (roundNum/10 != 0 && roundNum%10 != 0) {
        result = chinese_num[roundNum/10]+chinese_float[0]+chinese_num[roundNum%10]+chinese_float[1];
    }
    else if(roundNum/10 != 0 && roundNum%10 == 0)
    {
        result = chinese_num[roundNum/10]+chinese_float[0];
    }
    else if(roundNum/10 == 0 && roundNum%10 != 0)
    {
        result = chinese_num[0]+chinese_num[roundNum%10]+chinese_float[1];
    }
    else
    {
        result = "整";
    }
    return result;
}

//将输入数字整数部分分为4位一组
vector<LL> partition(LL inputNum)
{
    vector<LL> numVector;
    while (inputNum > 0) {
        LL num = inputNum%10000;
        numVector.push_back(num);
        inputNum /= 10000;
    }
    return numVector;
}

//4位数字为一个处理单元
string unit4(LL inputNum)
{
    if (inputNum == 0)
    {
        return chinese_num[0];
    }
    string unit = "";
    int pos = -1;
    bool flag = true;  //标识是否有连续的零
    while (inputNum > 0)
    {
        unit = ((inputNum%10==0)&&flag?"":chinese_num[inputNum%10] )+ (pos>=0&&inputNum%10!=0?chinese_unit[pos]:"") + unit;
        flag = (inputNum%10==0)?true:false;
        inputNum /= 10;
        pos++;
    }
    return unit;
}


//处理数字转换的主方法
string numToChineseNum(double num)
{
    string chineseNum = "";
    bool positive = isPositive(num);
    num = positive?num:(-1)*num;
    LL greaterThanZero = static_cast<LL>(num);
    vector<LL> numVec = partition(greaterThanZero);
    for (int i=0; i<numVec.size(); i++)
    {
        string numUnit = unit4(numVec[i]);
        if(numUnit == "零")
        {
            continue;
        }
        chineseNum = numUnit + chinese_bigunit[i] + chineseNum;
    }
    if(abs(greaterThanZero-num) > MIN)
    {
        chineseNum += processFloat(abs(greaterThanZero-num));
    }
    else
    {
        chineseNum += "整";
    }
    
    return positive?chineseNum:"负"+chineseNum;
}

int main(int argc, const char * argv[])
{
    cout<<"please input a number:"<<endl;
    double input;
    cin >> input;
    string result = numToChineseNum(input);
    cout<<"corresponding chinese num is: "<<endl<<result<<endl;
    return 0;
}


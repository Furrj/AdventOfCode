#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include "main.h"
using namespace std;

int main()
{
    string inputLine{};
    int santa_xPos{0};
    int santa_yPos{0};
    int robo_xPos{0};
    int robo_yPos{0};
    map<string, int> coordMap{};
    coordMap[formatCoords(0, 0)] = 1;
    int count{0};

    // Stream Init
    ifstream inputFile("inputs.txt");
    if (!inputFile.is_open())
    {
        cout << ("Error: could not open") << endl;
        return -1;
    }

    // Read Input
    while (!inputFile.eof())
    {
        inputFile >> inputLine;
    }

    // File Cleanup
    inputFile.close();

    for (char movement : inputLine)
    {
        if (count % 2 == 0)
        {
            switch (movement)
            {
            case '<':
                santa_xPos--;
                break;
            case '^':
                santa_yPos++;
                break;
            case '>':
                santa_xPos++;
                break;
            case 'v':
                santa_yPos--;
                break;
            }

            string coords = formatCoords(santa_xPos, santa_yPos);

            if (coordMap.find(coords) == coordMap.end())
            {
                coordMap[coords] = 1;
            }
            else
            {
                coordMap[coords] += 1;
            }
        }
        else
        {
            switch (movement)
            {
            case '<':
                robo_xPos--;
                break;
            case '^':
                robo_yPos++;
                break;
            case '>':
                robo_xPos++;
                break;
            case 'v':
                robo_yPos--;
                break;
            }

            string coords = formatCoords(robo_xPos, robo_yPos);

            if (coordMap.find(coords) == coordMap.end())
            {
                coordMap[coords] = 1;
            }
            else
            {
                coordMap[coords] += 1;
            }
        }
        count++;
    }

    cout << coordMap.size() << endl;

    return 0;
}

string formatCoords(int xPos, int yPos)
{
    return to_string(xPos) + "," + to_string(yPos);
}
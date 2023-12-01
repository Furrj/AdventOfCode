#include <iostream>
#include <vector>
#include <memory>
#include <fstream>
#include <algorithm>
#include "main.h"
using namespace std;

int main()
{
    string inputLine;
    int l{}, w{}, h{};
    unsigned long total{0};

    // Init
    ifstream inputFile("inputs.txt");
    if (!inputFile.is_open())
    {
        cout << ("Error: could not open") << endl;
        return -1;
    }

    // Caculations
    while (!inputFile.eof())
    {
        inputFile >> inputLine;
        getInputs(inputLine, l, h, w);
        total += calculateRibbon(l, h, w);
    }

    // Cleanup
    inputFile.close();

    cout << total << endl;

    return 0;
}

void getInputs(string inputLine, int &l, int &h, int &w)
{
    string l_str{""}, h_str{""}, w_str{""};
    int count{0};

    for (char c : inputLine)
    {
        switch (count)
        {
        case 0:
            if (c == 'x')
            {
                count++;
            }
            else
            {
                l_str += c;
            }
            break;
        case 1:
            if (c == 'x')
            {
                count++;
            }
            else
            {
                h_str += c;
            }
            break;
        case 2:
            w_str += c;
        }
    }

    l = stoi(l_str);
    h = stoi(h_str);
    w = stoi(w_str);
}

int calculateRibbon(int l, int h, int w)
{
    std::vector<int> sorted{l, h, w};
    sort(sorted.begin(), sorted.end());

    return (sorted.at(0) * 2) + (sorted.at(1) * 2) + (l * w * h);
}

int calculateGiftWrap(int l, int h, int w)
{
    const int a{l * h};
    const int b{l * w};
    const int c{h * w};

    unsigned short min{};
    min = (a <= b) ? a : b;
    min = (min <= c) ? min : c;

    return (2 * a) + (2 * b) + (2 * c) + min;
}
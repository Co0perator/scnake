#pragma once

#include <complex>
#include <vector>
#include <map>
#include <unordered_set>
#include "PyVar.hpp"

typedef enum
{
    strn,
    intr,
    flt,
    cmpx,
    lst,
    tpl,
    rng,
    dict,
    set,
    frzn,
    bol,
    byts,
    barr,
    memv,
    none,
} PyType;

//////////////////////////

class dictionary
{
public:
    std::vector<PyVar> keys;
    std::map<const PyVar, PyVar> hmap;
};

class range
{
private:
    const long long int start, stop, step;
    long long int value;
};

//////////////////////////

// Byte String(byts), Byte Array(barr), and Memory View(memv) functions here

//////////////////////////

typedef union
{
    char *strn;
    long long int intr;
    double flt;
    std::complex<double> cmpx;
    std::vector<PyVar> lst;
    const std::vector<PyVar> tpl;
    range rng;
    dictionary dict;
    std::unordered_set<PyVar> set;
    const std::unordered_set<PyVar> frzn;
    bool bol;
    void *byts;
    void *barr;
    void *memv;
    int *none;
} PyData;
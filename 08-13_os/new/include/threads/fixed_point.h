
/* prj1 imp hdr: use fixed point arithmatic */

#ifndef FIXED_POINT_H
#define FIXED_POINT_H

#include <stdint.h>

/*  0 1             17             31
	|s|     int     |     frxn     |
	0: sign, 1-16: integer part, 17-31: franctional part */
#define F (1<<14)

#define INT_TO_FP(n) (n * F)

#define FP_TO_INT_ROUND(x) (x / F)
#define FP_TO_INT(x) (x >= 0 ? (x + F/2) / F : (x - F/2) / F)

#define ADD_FP(x, y) (x + y)
#define ADD_MIX(x, n) (x + n*F)

#define SUB_FP(x, y) (x - y)
#define SUB_MIX(x, n) (x - n*F)

#define MUL_FP(x, y) (int)((((int64_t)x) * y) / F)
#define MUL_MIX(x, n) (x * n)

#define DIV_FP(x, y) (int)((((int64_t)x) * F) / y)
#define DIV_MIX(x, n) (x / n)

#endif FIXED_POINT_H /* threads/fixed_point.h */
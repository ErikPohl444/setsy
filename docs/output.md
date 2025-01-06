# Usage Walkthrough Markdown created by usage-vacuum from setsy.src.demo_usage.py

> [!NOTE]
>     demoing setsy class</br>    set up a setsy named first_setsy containing 3 elements</br>
```python
    first_setsy = setsy([6, 7, 8])
```
> [!NOTE]
>     output the powerset of the first_setsy</br>
```python
    print('here', list(first_setsy.powerset()))
```
here [(6,), (8, 7), (8,), (6, 7), (7,), (8, 6), (8, 6, 7), ()]
> [!NOTE]
>     set up a setsy named second_setsy containing 2 elements, each a set of 2 elements</br>
```python
    second_setsy = setsy([(1, 2), (1, 3)])
```
> [!NOTE]
>     is second_setsy a superset or subset of first_setsy?  we expect not.</br>
```python
    print(second_setsy.issubset(first_setsy))
```
False

```python
    print(second_setsy.issuperset(first_setsy))
```
False
> [!NOTE]
>     now union second setsy with first_setsy</br>
```python
    second_setsy = second_setsy.union(first_setsy)  # class setsy which inherits from set returns a set from union
```
> [!NOTE]
>     what do we get? hint: a setsy containing 2 sets of 2 elements each plus the 3 elements of first_setsy</br>
```python
    print(second_setsy)
```
{(1, 2), 6, 7, 8, (1, 3)}
> [!NOTE]
>     still a setsy.</br>
```python
    print(type(second_setsy))
```
<class 'setsy.setsy'>
> [!NOTE]
>     let's set up a third setsy called third_setsy</br>
```python
    third_setsy = {6, 5, 2, 1}
    print('------------')
```
------------
> [!NOTE]
>     what is the cartesian set of second_setsy and third_setsy?</br>
```python
    print(second_setsy.cartesian(third_setsy))
```
{((1, 2), 2), ((1, 2), 5), (8, 6), ((1, 3), 1), (6, 2), (7, 1), (6, 5), ((1, 2), 1), (8, 2), (8, 5), (6, 1), ((1, 3), 6), (7, 6), (8, 1), ((1, 2), 6), ((1, 3), 2), ((1, 3), 5), (7, 2), (6, 6), (7, 5)}
> [!NOTE]
>     NOW DO A REVIEW OF IS NOT SUBSET</br>    and a fourth setsy</br>
```python
    fourth_setsy = setsy([1, 2, 3])
```
> [!NOTE]
>     let's get its contents</br>
```python
    print("a:", fourth_setsy)
```
a: {1, 2, 3}
> [!NOTE]
>     redefine first_setsy to be more complicated</br>
```python
    first_setsy = setsy([2, 3, 4, 5, 6, 7])
```
> [!NOTE]
>     confirm its contents</br>
```python
    print("b:", first_setsy)
```
b: {2, 3, 4, 5, 6, 7}
> [!NOTE]
>     is fourth_setsy a subset of first_setsy?</br>
```python
    c = fourth_setsy.is_not_subset(first_setsy)
```
> [!NOTE]
>     and look: it knows why</br>
```python
    print("result of a.is_not_subset(b): ", c)
```
result of a.is_not_subset(b):  {1}

```python
    if c:
        print("a is not a subset of b")
```
a is not a subset of b

```python
    print("is not superset attempt")
```
is not superset attempt

```python
    fourth_setsy = setsy([1, 2, 3])
    print("a:", fourth_setsy)
```
a: {1, 2, 3}

```python
    first_setsy = setsy([2, 3, 4, 5, 6, 7])
    print("b:", first_setsy)
```
b: {2, 3, 4, 5, 6, 7}

```python
    c = first_setsy.is_not_superset(fourth_setsy)
    print("result of b.is_not_superset(a): ", c)
```
result of b.is_not_superset(a):  {1}

```python
    if c:
        print("b is not a superset of a")
```
b is not a superset of a

```python
    print("is not subset attempt")
```
is not subset attempt

```python
    fourth_setsy = setsy([2, 3])
    print("a:", fourth_setsy)
```
a: {2, 3}

```python
    first_setsy = setsy([2, 3, 4, 5, 6, 7])
    print("b:", first_setsy)
```
b: {2, 3, 4, 5, 6, 7}

```python
    c = fourth_setsy.is_not_subset(first_setsy)
    print("result of a.is_not_subset(b): ", c)
```
result of a.is_not_subset(b):  {}

```python
    print("a is not a subset of b") if c else print("a is a subset of b")
```
a is a subset of b

```python
    print("is not superset attempt")
```
is not superset attempt

```python
    fourth_setsy = setsy([2, 3])
    print("a:", fourth_setsy)
```
a: {2, 3}

```python
    first_setsy = setsy([2, 3, 4, 5, 6, 7])
    print("b:", first_setsy)
```
b: {2, 3, 4, 5, 6, 7}

```python
    c = first_setsy.is_not_superset(fourth_setsy)
    print("result of b.is_not_superset(a): ", c)
```
result of b.is_not_superset(a):  {}

```python
    if c:
    print("is not subset attempt")
```
is not subset attempt

```python
    fourth_setsy = setsy([2, 3])
    print("a:", fourth_setsy)
```
a: {2, 3}

```python
    first_setsy = setsy([2])
    print("b:", first_setsy)
```
b: {2}

```python
    c = fourth_setsy.is_not_subset(first_setsy)
    print("result of a.is_not_subset(b): ", c)
```
result of a.is_not_subset(b):  {3}

```python
    print("a is not a subset of b") if c else print("a is a subset of b")
```
a is not a subset of b

```python
    print("is not superset attempt")
```
is not superset attempt

```python
    fourth_setsy = setsy([2, 3])
    print("a:", fourth_setsy)
```
a: {2, 3}

```python
    first_setsy = setsy([2])
    print("b:", first_setsy)
```
b: {2}

```python
    c = first_setsy.is_not_superset(fourth_setsy)
    print("result of b.is_not_superset(a): ", c)
```
result of b.is_not_superset(a):  {3}

```python
    if c:
        print("b is not a superset of a")
```
b is not a superset of a

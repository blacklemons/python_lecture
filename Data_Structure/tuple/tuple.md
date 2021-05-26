# tuple

tuple은 수정이 불가능하다.

\# can't del

```python
t1 = (1, 2, 'a', 'b')
del t1[0]
```

```
Traceback (most recent call last): 
	File "<stdin>", line 1, in <module>
TypeError: 'tuple' object doesn't support item deletion
```

\# can't change

```python
t1[0] = 'c'
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

\# len() : return how many items a tuple has

\# list() , tuple() : tuple change to list / list change to tuple
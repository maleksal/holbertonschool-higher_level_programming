#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	PyObject *obj;
	Py_ssize_t length = PyList_Size(p);
	Py_ssize_t i = 0;

	printf("[*] Size of the Python List = %lu\n", length);
	printf("[*] Allocated = %lu\n", ((PyListObject *)(p))->allocated);

	for ( ; i < length; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %lu: %s\n", i, ((PyObject *)(p))->ob_type)
	}
}

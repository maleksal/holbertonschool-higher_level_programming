#include <Python.h>

void print_python_list_info(PyObject *p)
{
	PyObject *obj;
	Py_ssize_t length = PyList_Size(*p);
	Py_ssize_t i = 0;

	printf("[*] Size of the Python List = %lu\n", length);
	printf("[*] Allocated = %lu\n", ((PyVarObject *)(p))->ob_size);

	for ( ; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %zu: %s\n", i, Py_TYPE(obj)->ob_type)
	}



}

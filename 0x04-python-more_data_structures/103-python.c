#include <Python.h>
#include <stdio.h>


void print_python_bytes(PyObject *p)
{
	int i;
	long int size;
	char *buffer = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &buffer, &size);
	printf("  size: %li\n", size);
	printf("  trying string: %s\n", buffer);

	if (size < 10)
		printf("  first %li bytes:", (size + 1));
	else
	{
		printf("  first 10 bytes:");
	}
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02x", (unsigned char)buffer[i]);
	printf("\n");
}





void print_python_list(PyObject *p)
{
	PyObject *obj;
	Py_ssize_t length = PyList_Size(p);
	Py_ssize_t i = 0;

	(void) obj;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", length);
	printf("[*] Allocated = %lu\n", ((PyListObject *)(p))->allocated);

	for ( ; i < length; i++)
	{
		obj = PyList_GET_ITEM(p, i);
		printf("Element %lu: %s\n", i, obj->ob_type->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}

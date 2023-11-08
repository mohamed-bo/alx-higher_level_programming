#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - show basic information list pyobject
 * @p: adress of PyObject
 */

void print_python_list(PyObject *p)
{
	long unsigned int i, size;

	size = ((PyVarObject *)p)->ob_size;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %lu: %s\n", i,
			((PyListObject *)p)->ob_item[i]->ob_type->tp_name);
		if (!strcmp(((PyListObject *)p)->ob_item[i]->ob_type->tp_name, "bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[i]);
	}
}

/**
 * print_python_bytes - print object python information
 * @p: adress of python obejct
 */

void print_python_bytes(PyObject *p)
{
	long unsigned int size, firstbyteslen;
	char *s;
	long unsigned int i;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	s = ((PyBytesObject *)p)->ob_sval;
	size = ((PyVarObject *)p)->ob_size;
	firstbyteslen =  size + 1 > 10 ? 10 : size + 1;
	printf("  size: %lu\n", size);
	printf("  trying string: %s\n", s);
	printf("  first %lu bytes: ", firstbyteslen);
	for (i = 0; i < firstbyteslen; i++)
		printf("%02hhx%s", s[i], i + 1 < firstbyteslen ? " " : "");
	printf("\n");
}

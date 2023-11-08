#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - show basic information list pyobject
 * @p: adress of PyObject
 */

void print_python_list(PyObject *p)
{
	const char *tyype;
	int i;
	PyVarObject *obj = (PyVarObject *)p;
	PyListObject *list = (PyListObject *)p;
	int size = obj->ob_size;
	int allocat = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocat);
	for (i = 0; i < size; i++)
	{
		tyype = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, tyype);
		if (strcmp(tyype, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - print object python information
 * @p: adress of python obejct
 */

void print_python_bytes(PyObject *p)
{
	size_t size, firstbyteslen;
	char *s;
	int i;

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

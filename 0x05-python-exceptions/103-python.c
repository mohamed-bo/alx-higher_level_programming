#include <stdio.h>
#include <Python.h>


/**
 * print_python_bytes - print info about object
 * @p: adress of PyObject
 */

void print_python_bytes(PyObject *p)
{
	unsigned char i, numberFistPrinted;
	PyBytesObject *bytesVar = (PyBytesObject *)p;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytesVar->ob_sval);
	if (((PyVarObject *)p)->ob_size > 10)
		numberFistPrinted = 10;
	else
		numberFistPrinted = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes:", numberFistPrinted);
	for (i = 0; i < numberFistPrinted; i++)
		printf(" %02hhx", bytesVar->ob_sval[i]);
	printf("\n");
}

/**
 * print_python_float - print float python object info
 * @p: adress of PyObject
 */

void print_python_float(PyObject *p)
{
	char *s;
	double floa;

	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	floa = ((PyFloatObject *)p)->ob_fval;
	s = PyOS_double_to_string(floa, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", s);
}

/**
 * print_python_list - print some basic info about Python lists, Python bytes
 * @p: adress of PyObject
 */

void print_python_list(PyObject *p)
{
	const char *type;
	int i, size, alloca;
	PyListObject *pyList = (PyListObject *)p;
	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		size = ((PyVarObject *)p)->ob_size;
		alloca = pyList->allocated;
		printf("[*] Size of the Python List = %d\n", size);
		printf("[*] Allocated = %d\n", alloca);
		for (i = 0; i < size; i++)
		{
			type = pyList->ob_item[i]->ob_type->tp_name;
			printf("Element %d: %s\n", i, type);
			if (strcmp(type, "bytes") == 0)
				print_python_bytes(pyList->ob_item[i]);
			if (strcmp(type, "float") == 0)
				print_python_float(pyList->ob_item[i]);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}


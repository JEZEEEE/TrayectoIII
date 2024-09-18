from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria, Marca
from django.contrib import messages
from .forms import ProductoForm, CategoriaForm, MarcaForm

# Vista para listar productos
# def listar_productos(request):
#     productos = Producto.objects.all()
#     return render(request, 'productos/listar_productos.html', {'productos': productos})

def listar_productos(request):
    productos = Producto.objects.all()
    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()

    # Filtros
    marca_id = request.GET.get('marca')
    categoria_id = request.GET.get('categoria')
    precio_max = request.GET.get('precio')
    estado = request.GET.get('estado')

    if marca_id:
        productos = productos.filter(fky_mar=marca_id)
    if categoria_id:
        productos = productos.filter(fky_cat=categoria_id)
    if precio_max:
        productos = productos.filter(pre_prod__lte=precio_max)
    if estado:
        productos = productos.filter(est_prod=estado)

    context = {
        'productos': productos,
        'marcas': marcas,
        'categorias': categorias,
    }
    return render(request, 'productos/listar_productos.html', context)

# Vista para crear un nuevo producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/crear_producto.html', {'form': form})

# Vista para editar un producto
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')  # Redirigir a la lista de productos después de editar
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/editar_producto.html', {'form': form})

# Vista para eliminar un producto
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.est_prod = 'I'  # Asumimos que 'I' representa el estado inactivo o eliminado lógicamente.
    producto.save()
    messages.success(request, 'Producto desactivado correctamente.')
    return redirect('listar_productos')





# Vista para listar Categorías
def listar_categorias(request):
    categorias = Categoria.objects.all()

    # Obtener el filtro de estado
    estado = request.GET.get('estado')

    # Aplicar el filtro de estado si se seleccionó "Activo" o "Inactivo"
    if estado == 'A':
        categorias = categorias.filter(est_cat='A')
    elif estado == 'I':
        categorias = categorias.filter(est_cat='I')

    context = {
        'categorias': categorias,
    }
    return render(request, 'categorias/listar_categorias.html', context)


# Vista para crear una nueva Categoría
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/crear_categoria.html', {'form': form})

# Vista para editar una categoría
def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/editar_categoria.html', {'form': form, 'categoria': categoria})


# Vista para eliminar una categoría
def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    categoria.est_cat = 'I' # Asumimos que 'I' representa el estado inactivo o eliminado lógicamente.
    categoria.save()
    messages.success(request, 'Categoria desactivada correctamente.')
    return redirect('listar_categorias')



# Vista para listar Marcas
def listar_marcas(request):
    marcas = Marca.objects.all()

    # Obtener el filtro de estado
    estado = request.GET.get('estado')

    # Aplicar el filtro de estado si se seleccionó "Activo" o "Inactivo"
    if estado == 'A':
        marcas = marcas.filter(est_mar='A')
    elif estado == 'I':
        marcas = marcas.filter(est_mar='I')

    context = {
        'marcas': marcas,
    }
    return render(request, 'marcas/listar_marcas.html', context)


# Vista para crear una nueva Marca
def crear_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_marcas')
    else:
        form = MarcaForm()
    return render(request, 'marcas/crear_marca.html', {'form': form})



# Vista para editar una marca
def editar_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('listar_marcas')
    else:
        form = MarcaForm(instance=marca)
    return render(request, 'marcas/editar_marca.html', {'form': form, 'marca': marca})



def eliminar_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    marca.est_mar = 'I' # Asumimos que 'I' representa el estado inactivo o eliminado lógicamente.
    marca.save()
    messages.success(request, 'Marca desactivada correctamente.')
    return redirect('listar_marcas')



from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Producto

def generar_pdf_productos(request):
    # Crear una respuesta de tipo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="productos_registrados.pdf"'

    # Crear el PDF
    p = canvas.Canvas(response)

    # Título
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 800, "Lista de Productos Registrados")

    # Obtener los productos de la base de datos
    productos = Producto.objects.all()

    # Definir la posición inicial en el PDF
    y = 760

    # Encabezados de la tabla
    p.setFont("Helvetica-Bold", 12)
    p.drawString(80, y, "ID")
    p.drawString(150, y, "Nombre")
    p.drawString(300, y, "Precio")
    p.drawString(400, y, "Categoría")
    p.drawString(500, y, "Marca")
    p.drawString(600, y, "Estado")

    # Dibujar los productos en el PDF
    for producto in productos:
        y -= 20
        p.setFont("Helvetica", 10)
        p.drawString(80, y, str(producto.cod_prod))
        p.drawString(150, y, producto.nom_prod)
        p.drawString(300, y, str(producto.pre_prod))
        p.drawString(400, y, producto.fky_cat.nom_cat)
        p.drawString(500, y, producto.fky_mar.nom_mar)
        p.drawString(600, y, producto.est_prod)

        # Evitar que el texto se salga de la página
        if y < 50:
            p.showPage()
            y = 800

    # Finalizar el PDF
    p.showPage()
    p.save()

    return response

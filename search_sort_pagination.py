# You have to do imports!

def search_sort_pagination(table_name, field, keyword, orientation, ordtype, page, per_page):
    
    if ordtype == '':
        ordtype = id
    if orientation == '':
        get_items = table_name.query.filter(or_(getattr(table_name, field).contains(keyword)))
    elif orientation == 'asc':
        get_items = table_name.query.filter(or_(getattr(table_name, field).contains(keyword))).order_by(asc(ordtype))
    elif orientation == 'desc':
        get_items = table_name.query.filter(or_(getattr(table_name, field).contains(keyword))).order_by(desc(ordtype))

    items = []
    for item in get_items:
        items.append(getattr(item, field))  
    try:
        page = int(request.args.get('page'))
        per_page = int(request.args.get('per_page'))
    except:
        page = 1
        per_page = 50

    count = len(items)
    if count < page or per_page < 0:
        abort(404)
    obj = {}
    obj['count'] = count
    obj['results'] = items[((page-1)*per_page):((page-1)*per_page)+per_page]
    return jsonify(obj)
   
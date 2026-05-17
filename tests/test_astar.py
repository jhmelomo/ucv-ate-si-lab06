from lab6_intelligent_search.services.search_service import find_route

def test_astar_route():
    result = find_route('A', 'F')
    
    caminos_validos = [
        ['A', 'C', 'F'], 
        ['A', 'B', 'E', 'F']
    ]
    
    assert result['path'] in caminos_validos
    assert result['cost'] == 7
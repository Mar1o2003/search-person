from app import app, api
from app.resources import SearchResource, GetByIdResource, CreatePersonResource

api.add_resource(SearchResource, '/search')
api.add_resource(GetByIdResource, '/get_by_id')
api.add_resource(CreatePersonResource, '/create_person')

if __name__ == '__main__':
    app.run(debug=True)
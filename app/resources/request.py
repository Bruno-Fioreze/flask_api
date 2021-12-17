from flask_restful import reqparse


def only(params: list) -> dict:
    parser = reqparse.RequestParser()
    [parser.add_argument( param ) for param in params ]
    return parser.parse_args()
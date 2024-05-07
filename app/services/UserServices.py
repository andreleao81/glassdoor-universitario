from ..models.CurriculumModel import CurriculumModel
from ..extensions import ma
from ..models.UserModel import UserModel
from ..models.CollegeClassModel import CollegeClassModel


def get_history_by_user_id(userid) -> CurriculumModel:
    """
    Get a user's history
    """
    history = CurriculumModel.query.filter(
        CurriculumModel.user_id == userid
    ).order_by(CurriculumModel.semester).all()

    return history

# def get_history_by_user_id_done(user_id) -> CurriculumModel:
#     """
#     Get a user's done history
#     """
#     history = CurriculumModel.query.filter(
#         CurriculumModel.user_id == user_id,
#         CurriculumModel.conclusion == True
#     ).all().order_by(CurriculumModel.semester).asc()

#     return history

# def get_history_by_user_id_attending(user_id) -> CurriculumModel:
#     """
#     Get a user's attending history
#     """
#     history = CurriculumModel.query.filter(
#         CurriculumModel.user_id == user_id,
#         CurriculumModel.attending == True
#     ).all().order_by(CurriculumModel.semester).asc()

#     return history


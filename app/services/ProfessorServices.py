from app.models.ProfessorEvaluationModel import ProfessorEvaluationModel
from ..models.queries.Ratings import get_evals_by_prof



def get_professor_eval(prof_id, user_id, class_id):
    """
    Get a professor evaluation
    """
    professor_evaluation = ProfessorEvaluationModel.query.filter(
        ProfessorEvaluationModel.professor_id == prof_id,
        ProfessorEvaluationModel.user_id == user_id,
        ProfessorEvaluationModel.class_code == class_id
    ).first()

    if not professor_evaluation:
        return None

    return professor_evaluation



# def get_prof_overall(prof_id):
#     """
#     Get the score of a professor
#     """
#     prof_evals = get_evals_by_prof(prof_id)

#     if prof_evals == None:
#         return None
    
    
#     professor_evaluations_dicts = [evaluation._asdict() for evaluation in prof_evals]

#     # Convert the list of dictionaries to a DataFrame
#     df = pd.DataFrame(professor_evaluations_dicts)

#     # Calculate the mean of each column
#     mean_values = df.mean()

#     # Convert the result to a dictionary
#     mean_values_dict = mean_values.to_dict()

#     mean_attendance = mean_values_dict.get('attendance')
#     mean_punctuality = mean_values_dict.get('punctuality')
#     mean_availability_questions = mean_values_dict.get('availability_questions')
#     mean_student_relationship = mean_values_dict.get('student_relationship')
#     mean_professor_methodology = mean_values_dict.get('professor_methodology')

#     # Calculate the overall score
#     overall_score = (mean_attendance
#                      + mean_punctuality
#                      + mean_availability_questions 
#                      + mean_student_relationship 
#                      + mean_professor_methodology) / 5
    
#     return overall_score


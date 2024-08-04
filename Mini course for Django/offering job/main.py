import argparse

class ValidateNameException(BaseException):
    def __str__(self) -> str:
        return 'invalid name'
    
class ValidateTimetypeException(BaseException):
    def __str__(self) -> str:
        return 'invalid timetype'

class ValidateSalaryException(BaseException):
    def __str__(self) -> str:
        return 'invalid salary'

class ValidateAgeMinMaxException(BaseException):
    def __str__(self) -> str:
        return 'invalid age interval'

class ValidateAgeException(BaseException):
    def __str__(self) -> str:
        return 'invalid age'

class ValidateSkillIndexException(BaseException):
    def __str__(self) -> str:
        return 'invalid index'

class ValidateSkillLsitException(BaseException):
    def __str__(self) -> str:
        return 'invalid skill'

class ValidateSkillRepeatException(BaseException):
    def __str__(self) -> str:
        return 'repeated skill'
    

class Base:
    """ Base class for job and user"""
    def __init__(self, name: str, timetype: str, salary: int, list_skills: list) -> None:
        self.name = name
        self.timetype = timetype
        self.salary = salary
        Base.list_skills = list_skills

    
    def validate_name(self) -> bool:
        return (1 <= len(self.name) <= 10 and self.name.isalpha())
    
    def validate_timetype(self) -> bool:
        return self.timetype in ['FULLTIME', 'PARTTIME', 'PROJECT']
    
    def validate_salary(self) -> bool:
        return (0 <= self.salary < 1_000_000_000 and self.salary % 1000 == 0)
    
    @classmethod
    def validate_skill_list(cls, skill: str) -> bool:
        return skill in cls.list_skills
        

class Job(Base):
    """ class Job for validate and add job, adding viwe and job status"""
    job_id: int = 1
    job_list: dict = {}

    def __init__(self, name: str, minage: float, maxage: float, timetype: str, salary: int, list_skills: list) -> None:
        super().__init__(name, timetype, salary, list_skills)
        self.minage = minage
        self.maxage = maxage
        self.skill: list[str] = []
        self.view: list[int] = []

    def add_job(self) -> str:
        if self.validate():
            self.id = Job.job_id
            Job.job_id +=1
            Job.job_list.update({self.id: [self.name, self.minage, self.maxage,
                                            self.timetype, self.salary, self.skill, self.view]})
            return f'job id is {self.id}'

    def validate(self) -> bool:
        if self.validate_name() == False:
            raise ValidateNameException
        elif self.validate_age() == False:
            raise ValidateAgeMinMaxException
        elif self.validate_timetype() == False:
            raise ValidateTimetypeException
        elif self.validate_salary() == False:
            raise ValidateSalaryException
        else:
            return True
        
    def validate_age(self) -> bool:
        return (self.minage <= self.maxage and 0 <= self.minage <= 200 and 0 <= self.maxage <= 200)
    
    @classmethod
    def add_skill(cls, id: int, skill: str) -> str:
        if cls.validate_skill(id, skill):
            cls.job_list[id][5].append(skill)
            return 'skill added'

    @classmethod
    def validate_skill(cls, id:int, skill: str) -> bool:
        if cls.validate_skill_index(id) == False:
            raise ValidateSkillIndexException
        elif cls.validate_skill_list(skill) == False:
            raise ValidateSkillLsitException
        elif cls.validate_skill_repeat(id, skill) == True:
            raise ValidateSkillRepeatException
        else:
            return True 

    @classmethod
    def validate_skill_index(cls, id: int) -> bool:
        return id in cls.job_list.keys()
    
    @classmethod
    def validate_skill_repeat(cls, id: int, skill: str) -> bool:
        return skill in cls.job_list[id][5]
    
    @classmethod
    def add_view(cls, user_id: int, job_id: int) -> str:
        if user_id in User.user_list.keys() and job_id in cls.job_list.keys():
            cls.job_list[job_id][6].append(user_id)
            User.user_list[user_id][5].append(job_id)
            return 'tracked'
        else:
            raise ValidateSkillIndexException
        
    @classmethod
    def job_status(cls, job_id: int) -> str:
        if job_id in cls.job_list.keys():
            list_skill_user = []
            for skill in cls.job_list[job_id][5]:
                count_number_of_skill = 0
                for user in cls.job_list[job_id][6]:
                    if skill in User.user_list[user][4]:
                        count_number_of_skill +=1
                count_number_of_skill = (skill, count_number_of_skill)
                list_skill_user.append((count_number_of_skill[0], count_number_of_skill[1]))

            list_skill_user.sort(key=lambda x: x[0])
            list_skill_user.sort(key= lambda x: x[1])
            list_skill_user = [f'({i[0]},{str(i[1])})' for i in list_skill_user]
            list_skill_user = ''.join(list_skill_user)
            return f'{cls.job_list[job_id][0]}-{len(cls.job_list[job_id][6])}-{list_skill_user}'
        else:
            raise ValidateSkillIndexException


class User(Base):
    """ class User for validate and add user, user status and get job list"""
    user_id: int = 1
    user_list: dict = {}

    def __init__(self, name: str, age: float, timetype: str, salary: int, list_skills: list) -> None:
        super().__init__(name, timetype, salary, list_skills)
        self.age = age
        self.skill: list = []
        self.view: list =[]

    def add_user(self) -> str:
        if self.validate():
            self.id = User.user_id
            User.user_id +=1
            User.user_list.update({self.id: [self.name, self.age, self.timetype,
                                              self.salary, self.skill, self.view]})
            return f'user id is {self.id}'

    def validate(self) -> bool:
        if self.validate_name() == False:
            raise ValidateNameException
        elif self.validate_age() == False:
            raise ValidateAgeException
        elif self.validate_timetype() == False:
            raise ValidateTimetypeException
        elif self.validate_salary() == False:
            raise ValidateSalaryException
        else:
            return True
        
    def validate_age(self) -> bool:
        return (0 <= self.age <= 200)
    
    @classmethod
    def add_skill(cls, id: int, skill: str) -> str:
        if cls.validate_skill(id, skill):
            cls.user_list[id][4].append(skill)
            return 'skill added'

    @classmethod
    def validate_skill(cls, id:int, skill: str) -> bool:
        if cls.validate_skill_index(id) == False:
            raise ValidateSkillIndexException
        elif cls.validate_skill_list(skill) == False:
            raise ValidateSkillLsitException
        elif cls.validate_skill_repeat(id, skill) == True:
            raise ValidateSkillRepeatException
        else:
            return True 

    @classmethod
    def validate_skill_index(cls, id: int) -> bool:
        return id in cls.user_list.keys()
    
    @classmethod
    def validate_skill_repeat(cls, id: int, skill: str) -> bool:
        return skill in cls.user_list[id][4]
    
    @classmethod
    def user_status(cls, user_id: int) -> str:
        if user_id in cls.user_list.keys():
            list_skill_user = []
            for skill in cls.user_list[user_id][4]:
                count_number_of_skill = 0
                for job in cls.user_list[user_id][5]:
                    if skill in Job.job_list[job][5]:
                        count_number_of_skill +=1
                count_number_of_skill = (skill, count_number_of_skill)
                list_skill_user.append((count_number_of_skill[0], count_number_of_skill[1]))
            list_skill_user.sort(key=lambda x: x[0])
            list_skill_user.sort(key= lambda x: x[1])
            list_skill_user = [f'({i[0]},{str(i[1])})' for i in list_skill_user]
            list_skill_user = ''.join(list_skill_user)
            return f'{cls.user_list[user_id][0]}-{list_skill_user}'
        else:
            raise ValidateSkillIndexException

    @classmethod
    def get_job_list(cls, user_id: int) -> str:
        if user_id in cls.user_list.keys():
            list_points =[]
            for job_id, job_list in Job.job_list.items():
                point =0
                point += cls.point_age(user_id, job_list[1], job_list[2])
                point += cls.point_skills(user_id, job_list[5])
                point += cls.point_timetype(user_id, job_list[3])
                point += cls.point_salary(user_id, job_list[4])
                point = point*1000 + job_id
                list_points.append((job_id, int(point)))
            
            list_points.sort(key=lambda x: x[1], reverse=True)
            final_li =[]
            for i in list_points:
                final_li.append(f'({i[0]},{i[1]})')
                if len(final_li) == 5:
                    break
            return ''.join(final_li)
        else:
            raise ValidateSkillIndexException

    @classmethod
    def point_age(cls, user_id: int, min_age: float, max_age: float) ->float:
        x = cls.user_list[user_id][1]
        if min_age <= x <= max_age:
            return min(x - min_age, max_age - x)
        elif x > max_age:
            return max_age - x
        elif x < min_age:
            return x - min_age 
        
    @classmethod
    def point_skills(cls, user_id: int, job_skill: list) -> int:
        user_skill = set(cls.user_list[user_id][4])
        job_skill = set(job_skill)
        return 3*len(user_skill & job_skill) - len(job_skill - user_skill)
    
    @classmethod
    def point_timetype(cls, user_id: int, job_timetype: str) -> int:
        user_timetype = cls.user_list[user_id][2]
        if user_timetype == job_timetype:
            return 10
        elif (user_timetype == 'FULLTIME' and job_timetype == 'PROJECT') or (
            user_timetype == 'PROJECT' and job_timetype == 'FULLTIME'):
            return 4
        else:
            return 5
        
    @classmethod
    def point_salary(cls, user_id: int, job_salary: int) -> int:
        return 1000 // max(1, abs(job_salary- cls.user_list[user_id][3]))


def get_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    add_job = subparsers.add_parser('ADD-JOB',)
    add_job.add_argument(dest='data', nargs='+')

    add_user = subparsers.add_parser('ADD-USER',)
    add_user.add_argument(dest='data', nargs='+')

    add_job_skill = subparsers.add_parser('ADD-JOB-SKILL',)
    add_job_skill.add_argument(dest='data', nargs='+')
    
    add_user_skill = subparsers.add_parser('ADD-USER-SKILL',)
    add_user_skill.add_argument(dest='data', nargs='+')

    view = subparsers.add_parser('VIEW',)
    view.add_argument(dest='data', nargs='+')

    job_status = subparsers.add_parser('JOB-STATUS',)
    job_status.add_argument(dest='data', nargs='+')

    user_status = subparsers.add_parser('USER-STATUS',)
    user_status.add_argument(dest='data', nargs='+')

    get_joblist = subparsers.add_parser('GET-JOBLIST',)
    get_joblist.add_argument(dest='data', nargs='+')
    return parser


n = int(input())
list_skills = list(input().split())
parser = get_parser()
n = int(input())
for _ in range(n):
    req = vars(parser.parse_args(input().split()))
    command = req.pop("command")
    data = req['data']
    try:
        if command=="ADD-JOB":
            job = Job(data[0], float(data[1]), float(data[2]), data[3], int(data[4]), list_skills)
            print(job.add_job())
        elif command =="ADD-USER":
            user = User(data[0], float(data[1]), data[2], int(data[3]), list_skills)
            print(user.add_user())
        elif command=="ADD-JOB-SKILL":
            print(Job.add_skill(int(data[0]), data[1]))
        elif command=="ADD-USER-SKILL":
            print(User.add_skill(int(data[0]), data[1]))
        elif command=="VIEW":
            print(Job.add_view(int(data[0]), int(data[1])))
        elif command=="JOB-STATUS":
            print(Job.job_status(int(data[0])))
        elif command=="USER-STATUS":
            print(User.user_status(int(data[0])))
        elif command=="GET-JOBLIST":
            print(User.get_job_list(int(data[0])))
    except BaseException as b:
        print(b)
    except Exception as e:
        print(e)
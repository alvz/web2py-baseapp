# -*- coding: utf-8 -*-

def index():
    """
    Login page
    """
    if session.auth:
        redirect(URL('main', 'index'))
    else:
        form = auth.login()
        form.element()['_class']='form-inline well'
        form.element(_type='submit')['_class']='btn-primary custom-submit'
        return dict(form=form)


def logout():
    """
    Logout user
    """
    auth.logout()



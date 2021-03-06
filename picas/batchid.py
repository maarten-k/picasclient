# -*- coding: utf-8 -*-
from os import environ

''' @author Maarten Kooyman '''


def add_batch_management_id(doc):
    """
    Add job number id of the batch system to a token/document
    Adds information of the highest level of batch system,
    since job submision systems may be layered e.g:
    A glite wms system makes underneath use of a cream system which makes use
     of PBS. I such a case only the glite wms id instead of all of them.
    """
    wms_jobid = environ.get("GLITE_WMS_JOBID")
    cream_jobid = environ.get("CREAM_JOBID")
    pbs_jobid = environ.get("PBS_JOBID")
    slurm_jobid = environ.get("SLURM_JOBID")
    if str(wms_jobid).startswith("http"):
        doc["wms_job_id"] = wms_jobid
    elif cream_jobid is not None:
        doc["cream_job_id"] = cream_jobid
    elif pbs_jobid is not None:
        doc["pbs_job_id"] = pbs_jobid
    elif slurm_jobid is not None:
        doc["slurm_job_id"] = slurm_jobid


def remove_batch_management_id(doc):
    """
    removes all batch id from doc/token
    """
    if "wms_job_id" in doc:
        del doc["wms_job_id"]
    if "cream_job_id" in doc:
        del doc["cream_job_id"]
    if "pbs_job_id" in doc:
        del doc["pbs_job_id"]
    if "slurm_job_id" in doc:
        del doc["slurm_job_id"]

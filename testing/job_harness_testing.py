if __name__ == "__main__":
    import job_harness
    
    jh = job_harness.JobHarness()
    jh.job_name = 'xtbtest'
    #use absolute paths whenever possible
    jh.directory = '/gpfs/home/gdb20/code/batch-manager/scratch/test/'
    
    jh.manage_job()
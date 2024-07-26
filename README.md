# Quickly Validate RAK All-in-One 5G ECC608

- SSH to RAK All-in-One 5G device

- Execute command below to pull docker image

```
docker pull ghcr.io/herugen/ecc:latest
```

- Execute command below to run the docker container 

```
docker run -it --rm --privileged ghcr.io/herugen/ecc:latest
```

- The docker image runs a very simple logical, it just try to connect to ECC608 on the device.

- If connected succeed, it will print logs as below

```
root@rak-agw:/home/ubuntu# docker run -it --rm --privileged ghcr.io/herugen/ecc:latest
Congratulations!Connect ECC608 via I2C succeed
root@rak-agw:/home/ubuntu#
```

- If failed to connect, for example, run the docker on a MacBook which does not have such ECC608, it may show as below

```
herugen@00042-CN-SZ-RD-LAP-MAC afina % docker run -it --rm --privileged ghcr.io/herugen/ecc:latest
Traceback (most recent call last):
  File "ecc.py", line 25, in <module>
    ecc_cfg()
  File "ecc.py", line 20, in ecc_cfg
    raise EccError("Init ECC608 Error: {:d}".format(res))
__main__.EccError: Init ECC608 Error: 240
herugen@00042-CN-SZ-RD-LAP-MAC afina %
```




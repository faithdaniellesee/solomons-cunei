int __cdecl main(int argc, const char **argv, const char **envp)
{
  struct tm *v3; // rax
  unsigned int v4; // eax
  void *v5; // ST40_8
  FILE *v6; // ST38_8
  int result; // eax
  __int64 v8; // [rsp+48h] [rbp-178h]
  int v9; // [rsp+50h] [rbp-170h]
  int v10; // [rsp+54h] [rbp-16Ch]
  int v11; // [rsp+58h] [rbp-168h]
  int v12; // [rsp+5Ch] [rbp-164h]
  void *v13; // [rsp+80h] [rbp-140h]
  size_t v14; // [rsp+88h] [rbp-138h]
  FILE *v15; // [rsp+90h] [rbp-130h]
  char *v16; // [rsp+98h] [rbp-128h]
  __int64 v17; // [rsp+A4h] [rbp-11Ch]
  int v18; // [rsp+ACh] [rbp-114h]
  __int64 v19; // [rsp+B0h] [rbp-110h]
  int v20; // [rsp+B8h] [rbp-108h]
  int v21; // [rsp+BCh] [rbp-104h]
  int v22; // [rsp+C0h] [rbp-100h]
  int v23; // [rsp+C4h] [rbp-FCh]
  time_t v24; // [rsp+C8h] [rbp-F8h]
  int k; // [rsp+D0h] [rbp-F0h]
  int j; // [rsp+D4h] [rbp-ECh]
  int i; // [rsp+D8h] [rbp-E8h]
  const char **v28; // [rsp+E0h] [rbp-E0h]
  int v29; // [rsp+E8h] [rbp-D8h]
  int v30; // [rsp+ECh] [rbp-D4h]
  char v31[112]; // [rsp+F0h] [rbp-D0h]
  int v32[22]; // [rsp+160h] [rbp-60h]
  __int64 v33; // [rsp+1B8h] [rbp-8h]

  v30 = 0;
  v29 = argc;
  v28 = argv;
  v24 = time(0LL);
  v16 = (char *)argv[1];
  v15 = fopen(v16, "r");
  fseek(v15, 0LL, 2);
  v14 = ftell(v15);
  rewind(v15);
  v13 = calloc(1uLL, v14 + 1);
  fread(v13, 1uLL, v14, v15);
  fclose(v15);
  v3 = localtime(&v24);
  memcpy(&v8, v3, 0x38uLL);
  v23 = v12 + 1900;
  v22 = v11 + 1;
  v21 = v10;
  v20 = v9;
  v19 = v8;
  v18 = v9;
  v17 = v8;
  for ( i = 3; i > -1; --i )
  {
    v32[i] = v23 % 10;
    v23 /= 10;
  }
  for ( i = 5; i > 3; --i )
  {
    v32[i] = v22 % 10;
    v22 /= 10;
  }
  for ( i = 7; i > 5; --i )
  {
    v32[i] = v21 % 10;
    v21 /= 10;
  }
  for ( i = 9; i > 7; --i )
  {
    v32[i] = v20 % 10;
    v20 /= 10;
  }
  for ( i = 11; i > 9; --i )
  {
    v32[i] = SHIDWORD(v19) % 10;
    SHIDWORD(v19) /= 10;
  }
  for ( i = 13; i > 11; --i )
  {
    v32[i] = (signed int)v19 % 10;
    LODWORD(v19) = (signed int)v19 / 10;
  }
  for ( i = 15; i > 13; --i )
  {
    v32[i] = v18 % 10;
    v18 /= 10;
  }
  for ( i = 17; i > 15; --i )
  {
    v32[i] = SHIDWORD(v17) % 10;
    SHIDWORD(v17) /= 10;
  }
  for ( i = 19; i > 17; --i )
  {
    v32[i] = (signed int)v17 % 10;
    LODWORD(v17) = (signed int)v17 / 10;
  }
  for ( j = 0; *((_BYTE *)v13 + j); ++j )
  {
    if ( *((char *)v13 + j) < 97 || *((char *)v13 + j) > 122 )
    {
      if ( *((char *)v13 + j) >= 65 && *((char *)v13 + j) <= 90 )
      {
        *((_BYTE *)v13 + j) += LOBYTE(v32[j]);
        if ( *((char *)v13 + j) > 90 )
          *((_BYTE *)v13 + j) = *((_BYTE *)v13 + j) - 90 + 64;
        *((_BYTE *)v13 + j) = *((_BYTE *)v13 + j);
      }
    }
    else
    {
      *((_BYTE *)v13 + j) += LOBYTE(v32[j]);
      if ( *((char *)v13 + j) > 122 )
        *((_BYTE *)v13 + j) = *((_BYTE *)v13 + j) - 122 + 96;
      *((_BYTE *)v13 + j) = *((_BYTE *)v13 + j);
    }
  }
  for ( k = 14; k < 20; ++k )
    v31[k - 14] = *((_BYTE *)v13 + k);
  v4 = strlen(v31);
  v5 = (void *)str2md5(v31, v4);
  v6 = fopen("encrypt2.txt", "w");
  fwrite(v5, 4uLL, 8uLL, v6);
  fclose(v6);
  result = printf(
             "\n"
             "Find the secret message. Part of it is in Encrypt1.txt, encoded with base64. The rest of it has been hashed"
             ", Encrypt2.txt.\n",
             4LL);
  if ( __stack_chk_guard == v33 )
    result = 0;
  return result;
}
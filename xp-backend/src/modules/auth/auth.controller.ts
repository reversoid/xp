import {
  Body,
  Controller,
  NotImplementedException,
  Post,
  Query,
  ValidationPipe,
} from '@nestjs/common';
import { RegisterDTO } from './dto/register.dto';
import { AuthService } from './auth.service';
import { AuthQueryDTO } from './dto/auth.query.dto';
import { LoginDTO } from './dto/login.dto';

@Controller('auth')
export class AuthController {
  constructor(private authService: AuthService) {}

  @Post('register')
  async register(
    @Body() dto: RegisterDTO,
    @Query(
      new ValidationPipe({
        transform: true,
        forbidNonWhitelisted: true,
      }),
    )
    { suppress_tokens }: AuthQueryDTO,
  ) {
    const tokens = await this.authService.register(dto);

    if (suppress_tokens) {
      return;
    }

    throw new NotImplementedException({ tokens });
  }

  @Post('login')
  async login(
    @Body() dto: LoginDTO,
    @Query(
      new ValidationPipe({
        transform: true,
        forbidNonWhitelisted: true,
      }),
    )
    { suppress_tokens }: AuthQueryDTO,
  ) {
    const tokens = await this.authService.login(dto);

    if (suppress_tokens) {
      return;
    }

    throw new NotImplementedException({ tokens });
  }
}

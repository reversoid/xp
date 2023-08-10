import {
  Body,
  Controller,
  Get,
  Post,
  Query,
  ValidationPipe,
} from '@nestjs/common';
import { AuthService } from './auth.service';
import { LoginDTO } from './dto/login.dto';
import { RegisterDTO } from './dto/register.dto';
import { IsRegisteredQueryDTO } from './dto/is-registered.query.dto';

@Controller('auth')
export class AuthController {
  constructor(private authService: AuthService) {}

  @Post('register')
  async register(@Body() dto: RegisterDTO) {
    await this.authService.register(dto);
  }

  @Get('is_registered_tg')
  async isRegistered(
    @Query(
      new ValidationPipe({
        transform: true,
        forbidNonWhitelisted: true,
      }),
    )
    { tg_user_id }: IsRegisteredQueryDTO,
  ) {
    const registered = await this.authService.isRegisteredTg(tg_user_id);
    return { registered };
  }

  @Post('login')
  async login(@Body() dto: LoginDTO) {
    await this.authService.login(dto);
  }
}
